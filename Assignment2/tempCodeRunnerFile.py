while t > 1.e-9 and opt > 0:
        t *= sch
        newState = listEmploy

        # change state for new state
        changeState(newState,iMax,iMin)

        newOpt = optimal(newState)
        delta = newOpt[0] - opt
        print(delta)
        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / t):
            listEmploy = newState
            opt, iMax, iMin = newOpt
        if abs(opt) < 4:
            break