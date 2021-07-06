try:
    A = float(input("1st number: "))
    B = float(input("2st number: "))

    # power

    print(A**B)

    # modulus

    print(A%B)

    # divide with int result

    print(A//B)

except ValueError:
    print("please input integer or float")
