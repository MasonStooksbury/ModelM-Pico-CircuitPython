for col in cols:
        col.on()
        sleep_us(30) # Delay to let the GPIO settle a little
        for row in rows:
            now = ticks_ms()
            value = row.value()

            if (value != current_pin_state[col][row]) and (now - last_pin_state_change[col][row]) > debounceDelay:
                current_pin_state[col][row]
                last_pin_state_change[col][row] = now
        col.off()
        sleep_ms(1)



# for row in rows:
    #     row.on()
    #     for col in cols:
    #         value = col.value()
    #         if value:
    #             print(value)
    #     row.off()
    #     time.sleep_ms(1)

    # for col in cols:
    #     col.on()
    #     for row in rows:
    #         value = row.value()
    #         if value:
    #             print(value)
    #     col.off()
    #     sleep_ms(1)
        


a.on()
currentBtnState = s.value()
a.off()
current_time = ticks_ms()
if currentBtnState != previousBtnState:
    lastDebounceTime = current_time
if (current_time - lastDebounceTime) > debounceDelay:
    actualState = currentBtnState

if (previousActualState == 0) and (actualState == 1):
    count += 1
    print(count)

previousActualState = actualState
previousBtnState = currentBtnState
sleep_ms(1)










for col in cols:
        col['pin'].on()
        # sleep_us(30)
        for row in rows:
            value = row['pin'].value()
            if value:
                print(value)
        col['pin'].off()
        sleep_ms(1)
    


    # Constantly sends signals for some reason?
    # for row in rows:
    #     row['pin'].on()
    #     for col in cols:
    #         value = col['pin'].value()
    #         if value:
    #             print(value)
    #     row['pin'].off()
    #     sleep_ms(1)
        



# Works but needs some work with the delay. Currently at 4000
for col in cols:
    #     col['pin'].on()
    #     sleep_us(30) # Delay to let the GPIO settle a little
    #     for row in rows:
    #         now = ticks_ms()
    #         value = row['pin'].value()

    #         pin_change = pin_dict[col['name']][row['name']]['last_pin_state_change']
    #         pin_state = pin_dict[col['name']][row['name']]['current_pin_state']

    #         if (value != pin_state) and ((now - pin_change) > debounceDelay):
    #             pin_dict[col['name']][row['name']]['current_pin_state'] = value
    #             pin_dict[col['name']][row['name']]['last_pin_state_change'] = now
    #             count += 1
    #             print(count)
    #     col['pin'].off()
    #     sleep_ms(1)
     




# works pretty great

    for col in cols:
        col['pin'].on()
        for row in rows:
            pin_dict[col['name']][row['name']]['current_pin_state'] = row['pin'].value()
            current_time = ticks_ms()

            currentBtnState = pin_dict[col['name']][row['name']]['current_pin_state']

            if currentBtnState != pin_dict[col['name']][row['name']]['last_pin_state']:
                pin_dict[col['name']][row['name']]['last_debounce_time'] = current_time
            
            if (current_time - pin_dict[col['name']][row['name']]['last_debounce_time']) > debounceDelay:
                pin_dict[col['name']][row['name']]['actual_state'] = currentBtnState
            
            if (pin_dict[col['name']][row['name']]['last_actual_state'] == 0) and (pin_dict[col['name']][row['name']]['actual_state'] == 1):
                count += 1
                print(count)
            
            pin_dict[col['name']][row['name']]['last_actual_state'] = pin_dict[col['name']][row['name']]['actual_state']
            pin_dict[col['name']][row['name']]['last_pin_state'] = pin_dict[col['name']][row['name']]['current_pin_state']
        col['pin'].off()






# No debounce, but good for testing continuity
# for col in cols:
#     col['pin'].on()
#     # currentBtnState = r['pin'].value()
#     for row in rows:
#         state = row['pin'].value()
#         if state:
#             print(count)
#             count += 1
#     col['pin'].off()














# Columns
a = {'pin': Pin(0, Pin.OUT), 'name': 'a'}
b = {'pin': Pin(1, Pin.OUT), 'name': 'b'}
c = {'pin': Pin(2, Pin.OUT), 'name': 'c'}
d = {'pin': Pin(3, Pin.OUT), 'name': 'd'}
e = {'pin': Pin(4, Pin.OUT), 'name': 'e'}
f = {'pin': Pin(5, Pin.OUT), 'name': 'f'}
g = {'pin': Pin(6, Pin.OUT), 'name': 'g'}
h = {'pin': Pin(7, Pin.OUT), 'name': 'h'}
i = {'pin': Pin(8, Pin.OUT), 'name': 'i'}
j = {'pin': Pin(9, Pin.OUT), 'name': 'j'}
k = {'pin': Pin(10, Pin.OUT), 'name': 'k'}
l = {'pin': Pin(11, Pin.OUT), 'name': 'l'}
m = {'pin': Pin(12, Pin.OUT), 'name': 'm'}
n = {'pin': Pin(13, Pin.OUT), 'name': 'n'}
o = {'pin': Pin(14, Pin.OUT), 'name': 'o'}
p = {'pin': Pin(15, Pin.OUT), 'name': 'p'}

# Rows
q = {'pin': Pin(26, Pin.IN, Pin.PULL_DOWN), 'name': 'q'}
r = {'pin': Pin(22, Pin.IN, Pin.PULL_DOWN), 'name': 'r'}
s = {'pin': Pin(21, Pin.IN, Pin.PULL_DOWN), 'name': 's'}
t = {'pin': Pin(20, Pin.IN, Pin.PULL_DOWN), 'name': 't'}
u = {'pin': Pin(19, Pin.IN, Pin.PULL_DOWN), 'name': 'u'}
v = {'pin': Pin(18, Pin.IN, Pin.PULL_DOWN), 'name': 'v'}
w = {'pin': Pin(17, Pin.IN, Pin.PULL_DOWN), 'name': 'w'}
x = {'pin': Pin(16, Pin.IN, Pin.PULL_DOWN), 'name': 'x'}









# Columns
a = {'pin': Pin(0, Pin.IN, Pin.PULL_DOWN), 'name': 'a'}
b = {'pin': Pin(1, Pin.IN, Pin.PULL_DOWN), 'name': 'b'}
c = {'pin': Pin(2, Pin.IN, Pin.PULL_DOWN), 'name': 'c'}
d = {'pin': Pin(3, Pin.IN, Pin.PULL_DOWN), 'name': 'd'}
e = {'pin': Pin(4, Pin.IN, Pin.PULL_DOWN), 'name': 'e'}
f = {'pin': Pin(5, Pin.IN, Pin.PULL_DOWN), 'name': 'f'}
g = {'pin': Pin(6, Pin.IN, Pin.PULL_DOWN), 'name': 'g'}
h = {'pin': Pin(7, Pin.IN, Pin.PULL_DOWN), 'name': 'h'}
i = {'pin': Pin(8, Pin.IN, Pin.PULL_DOWN), 'name': 'i'}
j = {'pin': Pin(9, Pin.IN, Pin.PULL_DOWN), 'name': 'j'}
k = {'pin': Pin(10, Pin.IN, Pin.PULL_DOWN), 'name': 'k'}
l = {'pin': Pin(11, Pin.IN, Pin.PULL_DOWN), 'name': 'l'}
m = {'pin': Pin(12, Pin.IN, Pin.PULL_DOWN), 'name': 'm'}
n = {'pin': Pin(13, Pin.IN, Pin.PULL_DOWN), 'name': 'n'}
o = {'pin': Pin(14, Pin.IN, Pin.PULL_DOWN), 'name': 'o'}
p = {'pin': Pin(15, Pin.IN, Pin.PULL_DOWN), 'name': 'p'}

# Rows
q = {'pin': Pin(26, Pin.OUT), 'name': 'q'}
r = {'pin': Pin(22, Pin.OUT), 'name': 'r'}
s = {'pin': Pin(21, Pin.OUT), 'name': 's'}
t = {'pin': Pin(20, Pin.OUT), 'name': 't'}
u = {'pin': Pin(19, Pin.OUT), 'name': 'u'}
v = {'pin': Pin(18, Pin.OUT), 'name': 'v'}
w = {'pin': Pin(17, Pin.OUT), 'name': 'w'}
x = {'pin': Pin(16, Pin.OUT), 'name': 'x'}