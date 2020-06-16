"Coordinator--initiate-->Node0"

"Node0.wake()"

"Node0.status = Found"

"Node0--connect-->Node4"

"Node4.status = Found"

"Node4--connect-->Node0"


"Node0--initiate-->Node5"
"Node0--initiate-->Node1"
"Node0--initiate-->Node3"

"Node4--initiate-->Node2"
"Node4--initiate-->Node5"
"Node4--initiate-->Node3"

"Node0.status = Find"
"Node4.status = Find"

"Node0--Test-->Node5"
"Node4--Test-->Node2"

"Node5.wake()"
"Node2.wake()"

"Node5.status = Found"

"Node5--connect-->Node0"

"Node0.status = Found"

"Node0--connect-->Node5"

"Node0--Accept-->Node5"


"Node2.status = Found"

"Node2--connect-->Node4"

"Node4.status = Found"

"Node4--connect-->Node2"

"Node2--Accept-->Node4"


"Node0--Test-->Node1"
"Node4--Test-->Node5"

"Node5--initiate-->Node2"
"Node5--initiate-->Node4"

"Node2--initiate-->Node5"
"Node2--initiate-->Node3"

"Node2.status = Find"
"Node5.status = Find"

"Node1.status = Found"

"Node0.wake()"

"Node1--connect-->Node0"

"Node0.status = Found"

"Node0--connect-->Node1"

"Node1--Accept-->Node0"

"Node5--Reject-->Node4"

"Node0--Test-->Node3"
"Node4--Test-->Node3"


"Node3.status = Found"

"Node3.wake()"

"Node3--connect-->Node0"

"Node0.status = Found"

"Node0--connect-->Node3"

"Node3--Accept-->Node0"

"Node3--Reject-->Node4"


"Node1--initiate-->Node3"
"Node3--initiate-->Node4"
"Node3--initiate-->Node1"
"Node3--initiate-->Node2"

"Node5.status = Find"

"Node5--Test-->Node2"

"Node2--connect-->Node3"
"Node3--Reject-->Node2"

"Node5--Test-->Node4"

"Node2--connect-->Node3"
"Node3--Reject-->Node2"

"Node2--Test-->Node5"

"Node2--connect-->Node3"
"Node3--Reject-->Node2"


"Node2.status = Find"

"Node2--Test-->Node5"

"Node5--connect-->Node0"
"Node0--Reject-->Node5"

"Node2--Test-->Node3"

"Node2--connect-->Node3"
"Node3--Reject-->Node2"

"Node1.status = Find"

"Node1--Test-->Node3"

"Node3--Connect-->Node0"
"Node0--Reject-->Node3"

"Node3.status = Find"

"Node3--Test-->Node4"

"Node4--Connect-->Node0"
"Node0--Reject-->Node4"

"Node3--Test-->Node1"

"Node1--Connect-->Node0"
"Node0--Reject-->Node1"

"Node3--Test-->Node2"

"Node2--Connect-->Node5"
"Node5--Reject-->Node2"


The Edges in MST are: 0->5, 0->4, 0->1, 0->3, 4->2