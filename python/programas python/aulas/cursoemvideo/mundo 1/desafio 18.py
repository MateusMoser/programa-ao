import math
an = float(input('digite o angulo que voce deseja'))
seno= math.sin(math.radians(an))
print ('o angulo de {} tem o seno de {:.2f}'.format(an, seno))
cos = math.cos(math.radians(an))
print ('o angulo de {} tem o cosseno de {:.3}'.format(an,cos))
tan = math.tan(math.radians(an))
print ('o angulo de {} tem a tangente de {:.3}'.format (an,tan))
