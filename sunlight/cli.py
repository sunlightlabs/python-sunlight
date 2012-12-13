import json
import sys

from clint import args
import sunlight


def main():
    services = sunlight.available_services()
    service = services.get(args.get(0), None)

    if service is not None:
        available_methods = [
            m for m in dir(service) if not m.startswith('_') and m != 'get'
        ]
        if args.get(1) in available_methods:

            params = {
                g[0][2:]: g[1].get(0) for g in args.grouped.items()[1:] if
                g[0].startswith('--')
            }
            resp = getattr(service, args.get(1))(**params)
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
