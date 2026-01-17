def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    total_speed = 0
    redShirtSpeeds.sort()

    if not fastest:
        blueShirtSpeeds.sort(reverse=True)
    else:
        blueShirtSpeeds.sort()
    
    for idx in range(len(redShirtSpeeds)):
        redSpeed = redShirtSpeeds[idx]
        blueSpeed = blueShirtSpeeds[len(blueShirtSpeeds)-(idx+1)]
        total_speed += max(redSpeed,blueSpeed)
    return total_speed