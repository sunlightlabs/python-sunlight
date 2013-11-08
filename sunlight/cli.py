import json
import sys
import itertools

from clint import args
import sunlight
from sunlight.service import EntityList, EntityDict


def main():
    services = sunlight.available_services()
    service = services.get(args.get(0), None)

    if service is not None:
        available_methods = [
            m for m in dir(service) if not m.startswith('_') and m != 'get'
        ]
        if args.get(1) in available_methods:

            params = dict([
                (g[0][2:], g[1].get(0)) for g in args.grouped.items()[1:] if
                g[0].startswith('--')
            ])
            fn_args = [g.split(',') for g in args.grouped.get('_')[2:]]
            fn_args = list(itertools.chain.from_iterable(fn_args))
            resp = getattr(service, args.get(1))(*fn_args, **params)
            if isinstance(resp, EntityList) or isinstance(resp, EntityDict):
                resp = resp.data
            sys.stdout.write(json.dumps(resp, indent=2) + '\n')

        else:
            help(methods=available_methods)  # missing or invalid method param

    else:
        help(services=services)  # missing or invalid service parameter


def help(services=None, methods=None):
    sys.stderr.write("Usage: sunlight <service> <method> [<args>, ...]\n")

    if services:
        sys.stderr.write("Available services:\n")
        for s in services:
            sys.stderr.write("    %s\n" % s)

    if methods:
        sys.stderr.write("Available methods:\n")
        for m in methods:
            sys.stderr.write("    %s\n" % m)


if __name__ == "__main__":
    main()
