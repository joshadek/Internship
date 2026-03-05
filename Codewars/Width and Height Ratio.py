"""We all use 16:9, 16:10, 4:3 etc. ratios every day. Main task is to determine image ratio by its width and height dimensions.

Function should take width and height of an image and return a ratio string (ex."16:9"). If any of width or height entry is 0 function should throw an exception (or return Nothing).

"""

def calculate_ratio(w, h):
    if w == 0 or h == 0:
        return None

   
    common_divisor = 1
    for i in range(1, min(w, h) + 1):
        if w % i == 0 and h % i == 0:
            common_divisor = i

    w = w // common_divisor
    h = h // common_divisor

    return str(w) + ":" + str(h)


print (calculate_ratio(10, 15))