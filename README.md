# img_processing


RGB to HSI 

1. H = { theta       if B<=G       
      360-theta   if B > G
      
theta = cos^-1 { 1/2[(R-G) + (R-B)] /
                  [R-G]^2 + (R-B)(G-B)]^1/2       
                  
2. S = 1 - 3/(R+G+B)[min(R,G,B)]         
 
3. I = 1/3(R+G+B)          
 
 H = hue
 S = saturation
 I = intensity
 
 RGB degerleri [0,1] araligina normalize edildigini ve theta acisinin HSI uzayinda kirmizi eksenine gore olculdugu varsayilmaktadir. 
 Hue degerleri 1. esitlikte ile bulunan tum degerler 360 derece degerine bolunerek [0,1] araliginda normalize edilir.
 
 
 HSI to RGB
 
 RG kesimi (0 <= H < 120) H bu kesimden oldugunda RGB bilesenleri
 
 1. B = I(1-S)
 
 2. R = I[1+ S*cosH / cos(60 - H)]
 
 3. G = 3*I - (R+B)
 
 GB kesimi (120<= H < 240) Verilen H degeri bu kesimde ise ilk once  ondan 120 derece degerini cikaririz
 
 1. H = H - 120
 
 2. R = I(1-S)
 
 3. G = I(1+ S*cosH / cos(60 - H))
 
 4. B = 3*I - (R+G)
 
 
BR kesimi (240<= H < 360) Verilen H degeri bu kesimde ise ilk once onda 240 derecelik degeri cikaririz.

1. H = H - 240

2. G = I(1-S)

3.  B = I[1+ S*cosH / cos(60-H)]

4.  R = 3*I-(G+B)
 
 
