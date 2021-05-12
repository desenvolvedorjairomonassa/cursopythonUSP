def fizzbuzz(num):
    fizz = num%3 == 0
    buzz = num%5 == 0
    if fizz and buzz:
        return "FizzBuzz"
    elif fizz and not buzz:
        return "Fizz"
    elif not fizz and buzz:
        return "Buzz"
    else:
        return num

def test_fizz ():
    assert fizzbuzz(3) == "Fizz"

def test_buzz ():
    assert fizzbuzz(5) == "Buzz"

def test_fizzbuzz ():
    assert fizzbuzz(15) == "FizzBuzz"

def test_naodivisornem35 ():
    assert fizzbuzz(4) == 4
