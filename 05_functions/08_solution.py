def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

# print_kwargs(name="Shaktiman",power="Laser")
print_kwargs(power="super speed",name="Flash")
print_kwargs(name="Flash")
print_kwargs(power="super speed",name="Flash",enemy="Dr. Doom")