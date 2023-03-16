# Netbox initializer

Setup Netbox with custom Data and deploy VMs.

## execute

    git clone https://github.com/ThorstenHeck/netbox-ansible-custom
    cd netbox-ansible-custom
    ansible-playbook -i inventory playbooks/netbox_setup.yml
    ansible-playbook -i inventory playbooks/netbox_vm_update.yml