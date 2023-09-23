def truckTour(petrolpumps):
    for start in range(len(petrolpumps)):
        global truck_petrol
        truck_petrol = 0
        for i in range(len(petrolpumps)):
            cp = (start+i) % len(petrolpumps)
            truck_petrol += petrolpumps[cp][0]
            next_pump = petrolpumps[cp][1]
            if next_pump > truck_petrol:
                break
            truck_petrol -= next_pump
            
            if i == (len(petrolpumps)-1):
                return start

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()