def main():
    result1 = cubeVolume(2)
    result2 = cubeVolume(10)
    print(result1)
    print(result2)

def cubeVolume(sideLength):
    volume = sideLength ** 3
    return volume
main()
    
