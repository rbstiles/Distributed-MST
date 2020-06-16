# CS4113    -   Project1
    - Description
        * Implementation of the decentralized minimum spanning tree proposed by Gallagher, Humblet, and Spira using Python, gRPC, and Docker
    - Distributed MST/
        * Docs
            - Alpha.md
            - TestCasesMessage.md
            - TestCases.md
            * some additional pdfs and pngs
        * Node
            * NodeScripts
            - config.ini
            - Makefile
            - messenger.proto
            - node.py
            - Dockerfile
        * Scripts
            - clean_protos.sh
            - create_protos.sh
            - network_generator.py
            - run_locally.sh
        - .gitignore
        - COLLABORATORS
        - Makefile
        - README.md
        - docker-compose.yml
# Authors
    - Ryan
        - github: @rbstiles
    - Shubham
        - github: @shubham9482
    - Jared
        - github: @mulh8377



# Running the Project with Docker with Makefile (Create/Start/End)
    - make create_system
        - runs the script network_generator.py
            - redirects output to the docker-compose.yml file

    - make start_system
        - runs docker-compose up --build
            - Starts the system and deploys the container "cs4113project" with
                - node0
                - node1
                - node2
                - node3
                - node4
                - node5
                - server

    - make end_system
        - runs docker-compose down
            - End the system Tears down the container "cs4113project" with
                - node0
                - node1
                - node2
                - node3
                - node4
                - node5
                - server

### make create_system output
    - output
        python3 Scripts/network_generator.py > docker-compose.yml

### make start_system output
  - output
    <pre>Successfully built b59c911b6323
    Successfully tagged cs4113project_node4:latest
    Starting node3 ...
    Starting node1 ...
    Starting node3
    Starting node1
    Starting node4 ...
    Starting node2 ...
    Starting coordinator ...
    Starting node4
    Starting coordinator
    Starting node5 ...
    Starting node0 ...
    Starting node2
    Starting node5
    Starting node3 ... <font color="#4E9A06">done</font>
    Attaching to node0, node1, node2, coordinator, node5, node4, node3
    <font color="#06989A">node0     |</font> 2019-11-27 04:31:26,720 DEBUG:root node service start
    <font color="#C4A000">node1     |</font> 2019-11-27 04:31:26,712 DEBUG:root node service start
    <font color="#4E9A06">node2     |</font> 2019-11-27 04:31:26,704 DEBUG:root node service start
    <font color="#4E9A06">node2     |</font> node2 is running
    <font color="#06989A">node0     |</font> node0 is running
    <font color="#C4A000">node1     |</font> node1 is running
    <font color="#75507B">coordinator |</font> Nodes: 6
    <font color="#CC0000">node5     |</font> 2019-11-27 04:31:26,884 DEBUG:root node service start
    <font color="#75507B">coordinator |</font> Port: 50051
    <font color="#3465A4">node4     |</font> 2019-11-27 04:31:27,096 DEBUG:root node service start
    <font color="#CC0000">node5     |</font> node5 is running
    <font color="#75507B">coordinator |</font> [[&apos;node0&apos;, [&apos;node0&apos;, &apos;node1&apos;, &apos;node2&apos;, &apos;node3&apos;, &apos;node4&apos;, &apos;node5&apos;], [&apos;0&apos;, &apos;2&apos;, &apos;6&apos;, &apos;0&apos;, &apos;0&apos;, &apos;3&apos;]], [&apos;node1&apos;, [&apos;node0&apos;, &apos;node1&apos;, &apos;node2&apos;, &apos;node3&apos;, &apos;node4&apos;, &apos;node5&apos;], [&apos;2&apos;, &apos;0&apos;, &apos;0&apos;, &apos;0&apos;, &apos;9&apos;, &apos;0&apos;]], [&apos;node2&apos;, [&apos;node0&apos;, &apos;node1&apos;, &apos;node2&apos;, &apos;node3&apos;, &apos;node4&apos;, &apos;node5&apos;], [&apos;6&apos;, &apos;0&apos;, &apos;0&apos;, &apos;5&apos;, &apos;0&apos;, &apos;0&apos;]], [&apos;node3&apos;, [&apos;node0&apos;, &apos;node1&apos;, &apos;node2&apos;, &apos;node3&apos;, &apos;node4&apos;, &apos;node5&apos;], [&apos;0&apos;, &apos;0&apos;, &apos;5&apos;, &apos;0&apos;, &apos;4&apos;, &apos;0&apos;]], [&apos;node4&apos;, [&apos;node0&apos;, &apos;node1&apos;, &apos;node2&apos;, &apos;node3&apos;, &apos;node4&apos;, &apos;node5&apos;], [&apos;0&apos;, &apos;9&apos;, &apos;0&apos;, &apos;4&apos;, &apos;0&apos;, &apos;1&apos;]], [&apos;node5&apos;, [&apos;node0&apos;, &apos;node1&apos;, &apos;node2&apos;, &apos;node3&apos;, &apos;node4&apos;, &apos;node5&apos;], [&apos;3&apos;, &apos;0&apos;, &apos;0&apos;, &apos;0&apos;, &apos;1&apos;, &apos;0&apos;]]]
    <font color="#3465A4">node4     |</font> node4 is running
    <font color="#75507B">coordinator |</font> [&apos;node0&apos;, [&apos;node0&apos;, &apos;node1&apos;, &apos;node2&apos;, &apos;node3&apos;, &apos;node4&apos;, &apos;node5&apos;], [&apos;0&apos;, &apos;2&apos;, &apos;6&apos;, &apos;0&apos;, &apos;0&apos;, &apos;3&apos;]]
    <font color="#75507B">coordinator |</font> 2019-11-27 04:31:26,624 DEBUG:root coordinator start
    <font color="#34E2E2"><b>node3     |</b></font> 2019-11-27 04:31:27,624 DEBUG:root node service start
    <font color="#34E2E2"><b>node3     |</b></font> node3 is running
    <font color="#75507B">coordinator |</font> [&apos;node0&apos;, &quot;[&apos;node1&apos;, &apos;node2&apos;, &apos;node5&apos;]&quot;, &quot;[&apos;2&apos;, &apos;6&apos;, &apos;3&apos;]&quot;]
    <font color="#06989A">node0     |</font> Recieved: neighbors Message: [&apos;node0&apos;, &quot;[&apos;node1&apos;, &apos;node2&apos;, &apos;node5&apos;]&quot;, &quot;[&apos;2&apos;, &apos;6&apos;, &apos;3&apos;]&quot;]
    <font color="#06989A">node0     |</font> messeges[]: Recieved: neighbors Message: [&apos;node0&apos;, &quot;[&apos;node1&apos;, &apos;node2&apos;, &apos;node5&apos;]&quot;, &quot;[&apos;2&apos;, &apos;6&apos;, &apos;3&apos;]&quot;]
    <font color="#06989A">node0     |</font> 2019-11-27 04:31:30,744 DEBUG:root send---Recieved: neighbors Message: [&apos;node0&apos;, &quot;[&apos;node1&apos;, &apos;node2&apos;, &apos;node5&apos;]&quot;, &quot;[&apos;2&apos;, &apos;6&apos;, &apos;3&apos;]&quot;]---&gt;recieve
    <font color="#06989A">node0     |</font> 2019-11-27 04:31:30,744 DEBUG:root recieve---[&apos;node0&apos;, &quot;[&apos;node1&apos;, &apos;node2&apos;, &apos;node5&apos;]&quot;, &quot;[&apos;2&apos;, &apos;6&apos;, &apos;3&apos;]&quot;]---&gt;process_message---&gt;function
    <font color="#06989A">node0     |</font> 2019-11-27 04:31:30,744 DEBUG:root process_message---[&apos;node0&apos;, &quot;[&apos;node1&apos;, &apos;node2&apos;, &apos;node5&apos;]&quot;, &quot;[&apos;2&apos;, &apos;6&apos;, &apos;3&apos;]&quot;]---&gt;add_edges
    <font color="#06989A">node0     |</font> [&apos;node1&apos;, &apos;node2&apos;, &apos;node5&apos;]
    <font color="#06989A">node0     |</font> [&apos;2&apos;, &apos;6&apos;, &apos;3&apos;]
    <font color="#06989A">node0     |</font> Adjacent: node1, Weigh: 2, State: Basic
    <font color="#06989A">node0     |</font> Adjacent: node2, Weigh: 6, State: Basic
    <font color="#75507B">coordinator |</font> [&apos;node1&apos;, &quot;[&apos;node0&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;2&apos;, &apos;9&apos;]&quot;]
    <font color="#C4A000">node1     |</font> Recieved: neighbors Message: [&apos;node1&apos;, &quot;[&apos;node0&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;2&apos;, &apos;9&apos;]&quot;]
    <font color="#C4A000">node1     |</font> 2019-11-27 04:31:32,748 DEBUG:root send---Recieved: neighbors Message: [&apos;node1&apos;, &quot;[&apos;node0&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;2&apos;, &apos;9&apos;]&quot;]---&gt;recieve
    <font color="#C4A000">node1     |</font> messeges[]: Recieved: neighbors Message: [&apos;node1&apos;, &quot;[&apos;node0&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;2&apos;, &apos;9&apos;]&quot;]
    <font color="#C4A000">node1     |</font> 2019-11-27 04:31:32,748 DEBUG:root recieve---[&apos;node1&apos;, &quot;[&apos;node0&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;2&apos;, &apos;9&apos;]&quot;]---&gt;process_message---&gt;function
    <font color="#C4A000">node1     |</font> [&apos;node0&apos;, &apos;node4&apos;]
    <font color="#C4A000">node1     |</font> [&apos;2&apos;, &apos;9&apos;]
    <font color="#C4A000">node1     |</font> Adjacent: node0, Weigh: 2, State: Basic
    <font color="#C4A000">node1     |</font> 2019-11-27 04:31:32,748 DEBUG:root process_message---[&apos;node1&apos;, &quot;[&apos;node0&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;2&apos;, &apos;9&apos;]&quot;]---&gt;add_edges
    <font color="#75507B">coordinator |</font> [&apos;node2&apos;, &quot;[&apos;node0&apos;, &apos;node3&apos;]&quot;, &quot;[&apos;6&apos;, &apos;5&apos;]&quot;]
    <font color="#4E9A06">node2     |</font> Recieved: neighbors Message: [&apos;node2&apos;, &quot;[&apos;node0&apos;, &apos;node3&apos;]&quot;, &quot;[&apos;6&apos;, &apos;5&apos;]&quot;]
    <font color="#4E9A06">node2     |</font> messeges[]: Recieved: neighbors Message: [&apos;node2&apos;, &quot;[&apos;node0&apos;, &apos;node3&apos;]&quot;, &quot;[&apos;6&apos;, &apos;5&apos;]&quot;]
    <font color="#4E9A06">node2     |</font> 2019-11-27 04:31:34,751 DEBUG:root send---Recieved: neighbors Message: [&apos;node2&apos;, &quot;[&apos;node0&apos;, &apos;node3&apos;]&quot;, &quot;[&apos;6&apos;, &apos;5&apos;]&quot;]---&gt;recieve
    <font color="#4E9A06">node2     |</font> 2019-11-27 04:31:34,752 DEBUG:root recieve---[&apos;node2&apos;, &quot;[&apos;node0&apos;, &apos;node3&apos;]&quot;, &quot;[&apos;6&apos;, &apos;5&apos;]&quot;]---&gt;process_message---&gt;function
    <font color="#4E9A06">node2     |</font> 2019-11-27 04:31:34,752 DEBUG:root process_message---[&apos;node2&apos;, &quot;[&apos;node0&apos;, &apos;node3&apos;]&quot;, &quot;[&apos;6&apos;, &apos;5&apos;]&quot;]---&gt;add_edges
    <font color="#4E9A06">node2     |</font> [&apos;node0&apos;, &apos;node3&apos;]
    <font color="#4E9A06">node2     |</font> [&apos;6&apos;, &apos;5&apos;]
    <font color="#4E9A06">node2     |</font> Adjacent: node0, Weigh: 6, State: Basic
    <font color="#75507B">coordinator |</font> [&apos;node3&apos;, &quot;[&apos;node2&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;5&apos;, &apos;4&apos;]&quot;]
    <font color="#34E2E2"><b>node3     |</b></font> Recieved: neighbors Message: [&apos;node3&apos;, &quot;[&apos;node2&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;5&apos;, &apos;4&apos;]&quot;]
    <font color="#34E2E2"><b>node3     |</b></font> 2019-11-27 04:31:36,754 DEBUG:root send---Recieved: neighbors Message: [&apos;node3&apos;, &quot;[&apos;node2&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;5&apos;, &apos;4&apos;]&quot;]---&gt;recieve
    <font color="#34E2E2"><b>node3     |</b></font> messeges[]: Recieved: neighbors Message: [&apos;node3&apos;, &quot;[&apos;node2&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;5&apos;, &apos;4&apos;]&quot;]
    <font color="#34E2E2"><b>node3     |</b></font> 2019-11-27 04:31:36,754 DEBUG:root recieve---[&apos;node3&apos;, &quot;[&apos;node2&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;5&apos;, &apos;4&apos;]&quot;]---&gt;process_message---&gt;function
    <font color="#34E2E2"><b>node3     |</b></font> 2019-11-27 04:31:36,754 DEBUG:root process_message---[&apos;node3&apos;, &quot;[&apos;node2&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;5&apos;, &apos;4&apos;]&quot;]---&gt;add_edges
    <font color="#34E2E2"><b>node3     |</b></font> [&apos;node2&apos;, &apos;node4&apos;]
    <font color="#34E2E2"><b>node3     |</b></font> [&apos;5&apos;, &apos;4&apos;]
    <font color="#34E2E2"><b>node3     |</b></font> Adjacent: node2, Weigh: 5, State: Basic
    <font color="#75507B">coordinator |</font> [&apos;node4&apos;, &quot;[&apos;node1&apos;, &apos;node3&apos;, &apos;node5&apos;]&quot;, &quot;[&apos;9&apos;, &apos;4&apos;, &apos;1&apos;]&quot;]
    <font color="#3465A4">node4     |</font> Recieved: neighbors Message: [&apos;node4&apos;, &quot;[&apos;node1&apos;, &apos;node3&apos;, &apos;node5&apos;]&quot;, &quot;[&apos;9&apos;, &apos;4&apos;, &apos;1&apos;]&quot;]
    <font color="#3465A4">node4     |</font> 2019-11-27 04:31:38,756 DEBUG:root send---Recieved: neighbors Message: [&apos;node4&apos;, &quot;[&apos;node1&apos;, &apos;node3&apos;, &apos;node5&apos;]&quot;, &quot;[&apos;9&apos;, &apos;4&apos;, &apos;1&apos;]&quot;]---&gt;recieve
    <font color="#3465A4">node4     |</font> messeges[]: Recieved: neighbors Message: [&apos;node4&apos;, &quot;[&apos;node1&apos;, &apos;node3&apos;, &apos;node5&apos;]&quot;, &quot;[&apos;9&apos;, &apos;4&apos;, &apos;1&apos;]&quot;]
    <font color="#3465A4">node4     |</font> 2019-11-27 04:31:38,756 DEBUG:root recieve---[&apos;node4&apos;, &quot;[&apos;node1&apos;, &apos;node3&apos;, &apos;node5&apos;]&quot;, &quot;[&apos;9&apos;, &apos;4&apos;, &apos;1&apos;]&quot;]---&gt;process_message---&gt;function
    <font color="#3465A4">node4     |</font> [&apos;node1&apos;, &apos;node3&apos;, &apos;node5&apos;]
    <font color="#3465A4">node4     |</font> [&apos;9&apos;, &apos;4&apos;, &apos;1&apos;]
    <font color="#3465A4">node4     |</font> Adjacent: node1, Weigh: 9, State: Basic
    <font color="#3465A4">node4     |</font> 2019-11-27 04:31:38,756 DEBUG:root process_message---[&apos;node4&apos;, &quot;[&apos;node1&apos;, &apos;node3&apos;, &apos;node5&apos;]&quot;, &quot;[&apos;9&apos;, &apos;4&apos;, &apos;1&apos;]&quot;]---&gt;add_edges
    <font color="#3465A4">node4     |</font> Adjacent: node3, Weigh: 4, State: Basic
    <font color="#75507B">coordinator |</font> [&apos;node5&apos;, &quot;[&apos;node0&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;3&apos;, &apos;1&apos;]&quot;]
    <font color="#CC0000">node5     |</font> Recieved: neighbors Message: [&apos;node5&apos;, &quot;[&apos;node0&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;3&apos;, &apos;1&apos;]&quot;]
    <font color="#CC0000">node5     |</font> messeges[]: Recieved: neighbors Message: [&apos;node5&apos;, &quot;[&apos;node0&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;3&apos;, &apos;1&apos;]&quot;]
    <font color="#CC0000">node5     |</font> 2019-11-27 04:31:40,760 DEBUG:root send---Recieved: neighbors Message: [&apos;node5&apos;, &quot;[&apos;node0&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;3&apos;, &apos;1&apos;]&quot;]---&gt;recieve
    <font color="#CC0000">node5     |</font> 2019-11-27 04:31:40,760 DEBUG:root recieve---[&apos;node5&apos;, &quot;[&apos;node0&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;3&apos;, &apos;1&apos;]&quot;]---&gt;process_message---&gt;function
    <font color="#CC0000">node5     |</font> 2019-11-27 04:31:40,760 DEBUG:root process_message---[&apos;node5&apos;, &quot;[&apos;node0&apos;, &apos;node4&apos;]&quot;, &quot;[&apos;3&apos;, &apos;1&apos;]&quot;]---&gt;add_edges
    <font color="#CC0000">node5     |</font> [&apos;node0&apos;, &apos;node4&apos;]
    <font color="#CC0000">node5     |</font> [&apos;3&apos;, &apos;1&apos;]
    <font color="#CC0000">node5     |</font> Adjacent: node0, Weigh: 3, State: Basic
    <font color="#75507B">coordinator exited with code 0</font>
    <font color="#C4A000">node1     |</font> node1 has shut down
    <font color="#4E9A06">node2     |</font> node2 has shut down
    <font color="#06989A">node0     |</font> node0 has shut down
    <font color="#CC0000">node5     |</font> node5 has shut down
    <font color="#3465A4">node4     |</font> node4 has shut down
    <font color="#34E2E2"><b>node3     |</b></font> node3 has shut down
    <font color="#06989A">node0 exited with code 0</font>
    <font color="#4E9A06">node2 exited with code 0</font>
    <font color="#C4A000">node1 exited with code 0</font>
    <font color="#CC0000">node5 exited with code 0</font>
    <font color="#34E2E2"><b>node3 exited with code 0</b></font>
    <font color="#3465A4">node4 exited with code 0</font>
    </pre>


### make emd_system output
    - output
        docker-compose down
        Removing node0       ... done
        Removing node3       ... done
        Removing node2       ... done
        Removing node5       ... done
        Removing node1       ... done
        Removing node4       ... done
        Removing coordinator ... done
        Removing network cs4113project_default



## Update 11/5/19 20:31 : mulh8377
Added some files that still need to be implemented over the next week.
These are files currently empty and are awaiting implementation:

- CS4113-Project/
	- config.ini
	- network_generator.py
	- gallager.proto
	- Dockerfile
	- docker-compose.yml
	- node.py
	- COLLABORATORS

## Update 11/7/19 23:37 : mulh8377
Some stuff that I added will probably be deleted(poor implementation), so ignore some of the functions located in the Models Directory.

## Files Updated
- config.ini (working: from course website)
- network_generator.py (working: from course website)

## Files Added
- ./Client/client_node.py (note: needs further implementation)
- ./Client/Dockerfile (working docker build for the client_node)
- ./Client/gallagher.proto (note : needs further implementation)

- ./Server/server_node.py (note: needs further implementations)
- ./Server/Dockerfile (working docker build for the server_node)
- ./Server/config_reader.py (note: almost working needs some tweaks)
- ./Server/gallagher.proto (note : needs further implementation)


- Makefile (working: create_system, start_system, end_system)

## Notes

Please view the Makefile --- using these commands below work for creating a docker-compose file, building the machine, and tearing down the machine..

## Generate docker-compose.yml
make create_system

## Build and run the docker containers
make start_system

## Destroy the docker containers
make end_system

### Build Output (successful)
NOTE: node.py is not finished!
- Successfully built 331fc4fe28bb
- Successfully tagged cs4113project_node4:latest
- Creating coordinator ...
- Creating node4 ...
- Creating node1 ...
- Creating node2 ...
- Creating node0 ...
- Creating node5 ...
- Creating node3 ...
- Creating coordinator
- Creating node1
- Creating node4
- Creating node2
- Creating node0
- Creating node3
- Creating node0 ... done
- Attaching to node1, coordinator, node5, node2, node3, node4, node0
node1     | hey
coordinator | hey
node5     | hey
node3     | hey
node2      | hey
node4     | hey
node0     | hey
- node1 exited with code 0
- node5 exited with code 0
- coordinator exited with code 0
- node2 exited with code 0
- node3 exited with code 0
- node4 exited with code 0
- node0 exited with code 0



### Destroy Ouput (successful)
- Removing node5       ... done
- Removing node3       ... done
- Removing node0       ... done
- Removing node2       ... done
- Removing node4       ... done
- Removing node1       ... done
- Removing coordinator ... done
- Removing network cs4113project_default
