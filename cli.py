# coding:utf-8
import argparse
from block_chain import BlockChain

def new_parser():
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers(help='commands')
    # A print command
    print_parser = sub_parser.add_parser(
        'print', help='Print all the blocks of the blockchain')
    print_parser.add_argument('--print', dest='print', action='store_true')
    send_parser = sub_parser.add_parser(
        'send', help='Send AMOUNT of coins from FROM address to TO')
    send_parser.add_argument(
        '--from', type=str, dest='send_from', help='FROM')
    send_parser.add_argument(
        '--to', type=str, dest='send_to', help='TO')
    send_parser.add_argument(
        '--amount', type=int, dest='send_amount', help='AMOUNT')
    balance_parser = sub_parser.add_parser(
        'balance', help='Print balance of address')
    balance_parser.add_argument(type=str, dest='address', help='address')

    return parser

def print_chain(bc):
    for block in bc:
        print(block)

def get_balance(bc, addr):
    balance = 0
    utxos = bc.find_UTXO(addr)
    for utxo in utxos:
        balance += utxo.value
    print('%s balance is %d' %(addr, balance))

def send(bc, from_addr, to_addr, amount):
    bc = BlockChain()
    tx = bc.new_transaction(from_addr, to_addr, amount)
    bc.add_block([tx])
    print('send %d from %s to %s' %(amount, from_addr, to_addr))

def main():
    parser = new_parser()
    args = parser.parse_args()
    bc = BlockChain()
    if hasattr(args, 'print'):
        print_chain(bc)

    if hasattr(args, 'send_from') \
        and hasattr(args, 'send_to') \
        and hasattr(args, 'send_amount'):
        send(bc, args.send_from, args.send_to, args.send_amount)
    if hasattr(args, 'address'):
        get_balance(bc, args.address)

if __name__ == "__main__":
    main()