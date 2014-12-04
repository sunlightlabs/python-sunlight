import json
import itertools

from clint import arguments
from clint.textui import puts, puts_err, indent, colored
import sunlight


def main():
    args = arguments.Args()
    services = sunlight.available_services()
    service = services.get(args.get(0), None)

    if service is not None:
        available_methods = [
            m for m in dir(service) if not m.startswith('_') and m != 'get' and m != 'is_pageable'
        ]
        if args.get(1) in available_methods:

            params = dict([
                (f.strip('--'), args.value_after(f)) for f in args.flags.all
            ])
            fn_args = [g.split(',') for g in args.grouped.get('_')[2:]]
            fn_args = list(itertools.chain.from_iterable(fn_args))
            resp = getattr(service, args.get(1))(*fn_args, **params)
            meta = getattr(resp, '_meta', None)
            if meta:
                puts(colored.yellow(json.dumps(meta, indent=2)))
            puts(colored.blue(json.dumps(resp, indent=2) + '\n'))
        else:
            help(methods=available_methods)  # missing or invalid method param

    else:
        help(services=services)  # missing or invalid service parameter


def help(services=None, methods=None):
    puts_err("Usage: sunlight <service> <method> [<args>, ...]")

    if services:
        puts_err("Available services:")
        with indent(4):
            for s in services:
                puts_err(s)

    if methods:
        puts_err("Available methods:")
        with indent(4):
            for m in methods:
                puts_err(m)


if __name__ == "__main__":
    main()
