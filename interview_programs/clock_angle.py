def get_angle(hh,mm):
    hh = hh % 12
    hour_angle = hh * 30 + 0.5 * mm
    minute_angle = 6 * mm
    angle = abs(hour_angle-minute_angle)
    return min(angle,360-angle)

print(get_angle(8,32))