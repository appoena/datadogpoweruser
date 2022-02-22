FROM maven:3.6.0-jdk-11-slim AS build
WORKDIR /app
COPY . .
#Descomentar caso você queira buildar a aplicação. Obs.: Vai demorar um pouco(bastante)
#RUN mvn clean package

FROM openjdk:11-jre-slim
WORKDIR /app
COPY --from=build /app/target/spring-petclinic-2.6.0-SNAPSHOT.jar petclinic.jar


ENTRYPOINT ["java","-javaagent:./dd-java-agent.jar","-jar","./petclinic.jar"]