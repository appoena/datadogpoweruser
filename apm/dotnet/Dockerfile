FROM mcr.microsoft.com/dotnet/aspnet:5.0-buster-slim AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src/TodoApi
COPY . .
RUN dotnet build "TodoApi.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "TodoApi.csproj" -c Release -o /app/publish

FROM base AS final
COPY --from=publish /app/publish .
WORKDIR /opt/datadog
RUN apt-get update && apt-get install -y curl
RUN DATADOG_TRACE=2.0.1 && \
    curl -LO https://github.com/DataDog/dd-trace-dotnet/releases/download/v${DATADOG_TRACE}/datadog-dotnet-apm_${DATADOG_TRACE}_amd64.deb && \
    dpkg -i ./datadog-dotnet-apm_${DATADOG_TRACE}_amd64.deb && \
    rm -f /datadog-dotnet-apm_${DATADOG_TRACE}_amd64.deb
ENV CORECLR_ENABLE_PROFILING=1
ENV CORECLR_PROFILER={846F5F1C-F9AE-4B07-969E-05C26BC060D8}
ENV CORECLR_PROFILER_PATH=/opt/datadog/Datadog.Trace.ClrProfiler.Native.so
ENV DD_INTEGRATIONS=/opt/datadog/integrations.json
ENV DD_DOTNET_TRACER_HOME=/opt/datadog
WORKDIR /app
ENTRYPOINT ["dotnet", "TodoApi.dll"]