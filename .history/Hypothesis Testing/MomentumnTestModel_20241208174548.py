p l 1 t o t a l s e r v e s = 0
pl 1 w o n s e r v e s = 0
p l 2 t o t a l s e r v e s = 0
pl 2 w o n s e r v e s = 0
f o r p oi n t i n match :
i f e m p i r i c a l s t a r t re ached :
p = pl 1 w o n s e r v e s / p l 1 t o t a l s e r v e s
q = pl 2 w o n s e r v e s / p l 2 t o t a l s e r v e s
i f pl 1 s e r v i n g :
P( win ) = m a t c h p r o b a bili t y ( p , q ,
s c o r e )
i f pl 1 wins p oi n t :
pl 1 w o n s e r v e s += 1
p l 1 t o t a l s e r v e s += 1
i f pl 2 s e r v i n g :
P( win ) = 1 − m a t c h p r o b a bili t y ( q , p ,
s c o r e )
i f pl 2 wins p oi n t :
pl 2 w o n s e r v e s += 1
p l 2 t o t a l s e r v e s += 1