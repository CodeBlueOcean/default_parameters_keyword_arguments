#parameters
def say_hello(name, emoji):
    print(f'hellllooo {name}{emoji}')

#arguments
say_hello('Andrei', '😃') #call, invoke
say_hello('Dan', '😃') #call, invoke
say_hello('Dan', '😃') #call, invoke


# keyword arguments
say_hello(emoji='😀',
name='Bible')

# another example parameters
# Default Parameters
def say_hello(name='Darth Vader', emoji="😠"):
    print(f'hellllooo {name}{emoji}')

#arguments
say_hello('Andrei', '😃') #call, invoke
say_hello('Dan', '😃') #call, invoke
say_hello('Dan', '😃') #call, invoke


# keyword arguments
say_hello(emoji='😀',
name='Bible')
say_hello()

# keyword arguments
say_hello(emoji='😀',
name='Bible')
say_hello('Timmy')


