provider "aws" { region = var.region }

data "aws_ami" "selected" {
  most_recent = true
  owners      = ["amazon"]
  filter {
    name   = "name"
    values = [var.ami_filter]
  }
}

resource "aws_instance" "this" {
  count                  = length(var.subnet_ids)
  ami                    = data.aws_ami.selected.id
  instance_type          = var.instance_type
  subnet_id              = var.subnet_ids[count.index]
  vpc_security_group_ids = var.security_group_ids
  key_name               = var.key_name
  tags = {
    Name        = "${var.name}-${count.index}"
    Environment = "qa"
  }
}
