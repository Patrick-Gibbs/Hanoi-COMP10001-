def hanoi(to, _from, via, n):
    """
    Solves the towers of hanoi problem
    example: https://en.wikipedia.org/wiki/Tower_of_Hanoi

    input:
        `to`: The name of the stake that the tokens should be moved to
        `_from`: The name of the stake that the tokens are moved from
        `via`: The name of the stake that starts empty
        `n`: The number of tokens on the initial stake
    output: None
            Solution printed to terminal
    
            
    Example call: hanoi('c', 'a', 'b', 3)
    """


    if n == 1:
        print(f'move from {_from} to {to}')
    else:
        hanoi(via, _from, to, n-1)
        print(f'move from {_from} to {to}')
        hanoi(to, via, _from, n-1)

hanoi('c', 'a', 'b', 24)