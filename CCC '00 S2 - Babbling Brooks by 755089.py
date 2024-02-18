#-----------------------------------------------------------------------------
# Name:  CCC '00 S2 - Babbling Brooks (main.py)
# Author:      Aryan Mittal
# Created:     17-Feb-2024
# Updated:     17-Feb-2024
#---------------------------------------------------------------------------
initialNumberOfStreams = int(input())
streamFlows = []

# Collects initial stream flows
for _ in range(initialNumberOfStreams):
    initialStreamFlow = int(input())
    streamFlows.append(initialStreamFlow)

action = int(input())
# Processes actions until termination
while action != 77:
    if action == 99:  # Splits the action
        streamSplitPoint = int(input()) - 1
        originalStreamFlow = streamFlows[streamSplitPoint]
        streamFlowPercentageToLeft = int(input())
        # Update flows after split
        leftStreamFlow = originalStreamFlow * (streamFlowPercentageToLeft / 100)
        rightStreamFlow = originalStreamFlow * (1 - (streamFlowPercentageToLeft / 100))
        streamFlows[streamSplitPoint] = leftStreamFlow
        streamFlows.insert(streamSplitPoint + 1, rightStreamFlow)
    else:  # Joins the action
        streamJoinPoint = int(input()) - 1
        # Combines the flows after join
        streamFlows[streamJoinPoint] += streamFlows[streamJoinPoint + 1]
        streamFlows.pop(streamJoinPoint + 1)
    action = int(input())

# Outputs the flow in each river
for i in range(len(streamFlows) - 1):
    print(f"{int(streamFlows[i])}", end=" ")
print(f"{int(streamFlows[-1])}")