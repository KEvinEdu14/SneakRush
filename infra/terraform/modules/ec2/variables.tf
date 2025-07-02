variable "region"              { type = string }
variable "name"                { type = string }
variable "instance_type"       { type = string }
variable "ami_filter"          { type = string }
variable "subnet_ids"          { type = list(string) }
variable "security_group_ids"  { type = list(string) }
variable "key_name"            { type = string }
