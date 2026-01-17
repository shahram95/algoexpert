def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    frontRow = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'

    for idx in range(len(redShirtHeights)):
        if frontRow == 'RED' and redShirtHeights[idx] >= blueShirtHeights[idx]:
            return False
        elif frontRow == 'BLUE' and blueShirtHeights[idx] >= redShirtHeights[idx]:
            return False

    return True