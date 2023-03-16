# Netbox initializer

Setup Netbox with custom Data and deploy VMs.

## execute

    git clone https://github.com/ThorstenHeck/netbox-fork
    cd netbox-fork
    ansible-playbook -i inventory playbooks/netbox_setup.yml
    ansible-playbook -i inventory playbooks/netbox_vm_update.yml