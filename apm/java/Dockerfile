FROM maven:3.6.0-jdk-11-slim AS build
WORKDIR /app
COPY . .
RUN mvn clean package

FROM eclipse-temurin:11-jre-alpine
WORKDIR /app
COPY --from=build /app/target/spring-java-0.0.1-SNAPSHOT.jar spring-java.jar


ENTRYPOINT ["java","-jar","./spring-java.jar"]
