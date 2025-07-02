provider "aws" { region = var.region }

resource "aws_db_subnet_group" "this" {
  name       = "${var.db_name}-subnet-group"
  subnet_ids = var.subnet_ids
}

resource "aws_db_instance" "this" {
  identifier             = "qa-${var.db_name}"
  engine                 = "postgres"
  engine_version         = var.engine_version
  instance_class         = var.instance_class
  allocated_storage      = var.allocated_storage
  name                   = var.db_name
  username               = var.username
  password               = var.password
  db_subnet_group_name   = aws_db_subnet_group.this.name
  vpc_security_group_ids = var.vpc_security_group_ids
  skip_final_snapshot    = true
}
