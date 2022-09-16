##میوه‌خوری

def fruits(fruit_list):
    result_dict = {}

    for f in range(len(fruit_list)):
        # شکل آن به صورت کروی (sphere) باشد.
        # جرم آن بین ۳۰۰ تا ۶۰۰ گرم باشد.
        # حجم آن بین ۱۰۰ تا ۵۰۰ سانتی‌متر مکعب باشد.
        if (fruit_list[f].get("shape") == "sphere" and 300 <= fruit_list[f].get("mass") <= 600 and 100 <= fruit_list[
            f].get("volume") <= 500):

            count = 1
            if (fruit_list[f].get("name")) in result_dict:
                count = result_dict[(fruit_list[f].get("name"))] + 1
            result_dict[fruit_list[f].get("name")] = count
    return (result_dict)


fruits((
    {'name': 'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name': 'mango', 'shape': 'square', 'mass': 150, 'volume': 120},
    {'name': 'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name': 'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}))
