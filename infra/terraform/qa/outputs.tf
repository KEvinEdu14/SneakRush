output "postgres_endpoint" {
  value = module.postgres.endpoint
}

output "auth_service_ip" {
  value = module.auth_service.public_ips[0]
}
