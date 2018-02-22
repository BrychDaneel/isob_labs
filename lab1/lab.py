import cesar
import visin
import argparse
import sys


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-v', action='store_const', const=True)
    ap.add_argument('-d', action='store_const', const=True)
    ap.add_argument('key')
    args = ap.parse_args()

    if args.v:
        module = visin
        key = args.key
    else:
        module = cesar
        key = int(args.key)

    if args.d:
        fun = module.dencrypt
    else:
        fun = module.encrypt

    inp = sys.stdin.read()
    out = fun(inp, key)
    print(out)
