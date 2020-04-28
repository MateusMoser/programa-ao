
water = int(input('Write how many ml of water the coffee machine has:'))
milk = int(input('Write how many ml of milk the coffee machine has:'))
coffee = int(input('Write how many grams of coffee beans the coffee machine has:'))
cups = int(input('Write how many cups of coffee you will need:'))

wn = cups*200
mn = cups*50
cn = cups*15



if wn == water and milk == mn and coffee == cn:
    print("Yes, I can make that amount of coffee")
if wn > water or mn > milk or cn > coffee:
    pc1 = water//200
    pc2 = milk//50
    pc3 = coffee//15
    pc=[pc1,pc2,pc3]
    print(f"No, I can make only {min(pc)} cups of coffee")
else:
    wd = water - wn  # water diff = water - water needed
    pc1 = wd / 200  # possible cups = water difference / 200
    md = milk - mn
    pc2 = md / 50
    cd = coffee - cn
    pc3 = cd / 15
    pc = [pc1, pc2, pc3]
    print("Yes, I can make that amount of coffee (and even %i more than that)" % min(pc))
