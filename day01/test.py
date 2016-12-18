from taxiCab import taxiCab
from router import router

test_cab = taxiCab(0,0,0)
test_router = router(test_cab)

o = taxiCab(0,0,0)
a = taxiCab(5,0,0)
b = taxiCab(5,1,0)
c = taxiCab(4,1,0)
d = taxiCab(4,-5,0)
f = taxiCab(-1,-5,0)
g = taxiCab(-1,0,0)
h = taxiCab(3,0,0)

print test_router.intersects(a,b,c,d)
print test_router.intersects(o,a,c,d)
print test_router.intersects(o,a,g,h)

print "Testing ..."

a = taxiCab(8,0,0)
b = taxiCab(8,-4,0)
c = taxiCab(4,-4,0)
d = taxiCab(4,4,0)

print test_router.intersects(o,a,c,d)
test_router.update_intersection(o,a,c,d)
print test_router.intersect_point.x
print test_router.intersect_point.y

print "Testing 2...."
a = taxiCab(-3,0,0)
b = taxiCab(-3,1,0)
c = taxiCab(-7,1,0)
d = taxiCab(-7,0,0)
print test_router.intersects(o,a,c,d)
