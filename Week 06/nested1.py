# Nested loop Example 1
# the inner loop iterates completely (4 times) for every one iteration
# of the outer loop

# CSC 110

for outer in [1, 2, 3]:
    print 'Outer loop iteration', outer
    for inner in [1, 2, 3, 4]:
        print '    Inner loop iteration', inner
    
