# Kafka Message Keys and Offset 
# Download Kafka by running the command below:
wget https://downloads.apache.org/kafka/3.7.0/kafka_2.12-3.7.0.tgz

# Extract Kafka from the zip file by running the command below.
tar -xzf kafka_2.12-3.7.0.tgz

#  Configure KRaft and start server:
# Change to the kafka_2.12-3.7.0 directory:
cd kafka_2.12-3.7.0

# Generate a Cluster UUID that will uniquely identify the Kafka cluster:
KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"

# KRaft requires the log directories to be configured. Run the following command to configure the log directories passing the cluster ID:
bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties

# Now that KRaft is configured, you can start the Kafka server by running the following command:
bin/kafka-server-start.sh config/kraft/server.properties

# Create a topic and producer for processing bank ATM transactions :
# Open a new terminal and change to the kafka_2.12-3.7.0 directory :
cd kafka_2.12-3.7.0

# Create a new topic using the --topic argument with the name bankbranch. To simplify the topic configuration and better explain how message key and consumer offset work, you specify the --partitions 2 argument to create two partitions for this topic.
# To compare the differences, you may try other partitions settings for this topic:
bin/kafka-topics.sh --create --topic bankbranch --partitions 2 --bootstrap-server localhost:9092

# List all topics to check if bankbranch has been created successfully:
bin/kafka-topics.sh --bootstrap-server localhost:9092 --list

# You can also use the --describe command to check the details of the topic bankbranch:
bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic bankbranch

# Run the following command in the same terminal window with the topic details to create a producer for the topic bankbranch:
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic bankbranch

# To produce the messages, look for the > icon and add the following ATM messages after the icon:
{"atmid": 1, "transid": 100}
{"atmid": 1, "transid": 101}
{"atmid": 2, "transid": 200}
{"atmid": 1, "transid": 102}
{"atmid": 2, "transid": 201}


# Open a new terminal and change to the kafka_2.12-3.7.0 directory:
cd kafka_2.12-3.7.0

# Then start a new consumer to subscribe to the bankbranch topic:
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic bankbranch --from-beginning