def unique(l):
    if len(l) == len(set(l)):  # so sanh do dai l va do dai cua tap hop cua l
        print("Tat ca phan tu la duy nhat")
    else:
        print("list co phan tu trung lap")


unique([1, 2, 3, 4])

unique([1, 1, 3, 4])
