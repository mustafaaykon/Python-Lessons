def CustomStrip(param, *chars):
    i = 0
    while i < (len(chars)**2):
        if param[0] in chars:
            param = param.strip(param[0])

        if(param[len(param) - 1] in chars):
            param = param.strip(param[len(param) - 1])
        i += 1
    return param


result = CustomStrip('&@?-_BilgeAdam Beşiktaş&@?-_',  '@', '?', '-', '_', '&')
print(result)

# Bilge Adam Beşiktaş
# Bilge Adam Beşiktaş
# &@?-_Bilge Adam Beşiktaş
# Bilge Adam Beşiktaş


# murat.vuranok@bilgeadam.com


# isim = murat
# soyisim = vuranok
# firma = bilgeadam
# uzanti = com
# mail adresi =
