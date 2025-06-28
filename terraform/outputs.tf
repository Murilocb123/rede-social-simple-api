output "ip_publico_da_instancia" {
  description = "Endereço IP da instância EC2"
  value       = aws_instance.rede_social_api.public_ip
}