

def getMinCost(crew_id, job_id):
    crew_id.sort()
    job_id.sort()
    minTravel = 0
    
    for i in range(len(crew_id)):
        if job_id[i] >= crew_id[i]:
            t = job_id[i] - crew_id[i]
            minTravel += t
        else:
            t = crew_id[i] - job_id[i]
            minTravel += t
    return minTravel
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    crew_id_count = int(input().strip())

    crew_id = []

    for _ in range(crew_id_count):
        crew_id_item = int(input().strip())
        crew_id.append(crew_id_item)

    job_id_count = int(input().strip())

    job_id = []

    for _ in range(job_id_count):
        job_id_item = int(input().strip())
        job_id.append(job_id_item)

    result = getMinCost(crew_id, job_id)

    fptr.write(str(result) + '\n')

    fptr.close()
