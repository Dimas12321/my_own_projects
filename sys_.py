def main():
    ocenki = []
    n = int(input('How many ocenok: '))

    for a in range(1,n+1):
        print(f"Ocenka #{a}: ",end='', sep='')
        x = float(input(': '))
        
        ocenki.append(x)
    
    print("Middle-ariphetic: ",process(ocenki))

def process(ocenki):
    total = int(sum(ocenki))// len(ocenki)
    return total

main()
input()