buying = input('would you want a muffin or cupcake?')
muffins = 10
cupcakes = 10

while buying != "0":
    if buying == "muffin" and muffins > 0:
        muffins -=1
        print(f"One Muffin bought. There are {muffins} left")
    if buying == "muffin" and muffins == 0:
            print('OUT OF STOCK')
            
    if buying == "cupcake" and cupcakes > 0:
        cupcakes -=1
        print(f"One cupcake bought. There are {cupcakes} left")
    if buying == "cupcake" and cupcakes == 0:
            print('OUT OF STOCK')
        
        
    buying = input('would you want a muffin or cupcake?')

print("muffins:", muffins, "cupcakes:", cupcakes)


        
