# Netbox initializer

Setup Netbox with custom Data and deploy VMs.

## execute
    export NETBOX_API_KEY=SECRET_TOKEN_CHANGE_ME
    export NETBOX_URL=http://65.21.252.14:8000

    git clone https://github.com/ThorstenHeck/netbox-ansible-custom
    cd netbox-ansible-custom
    ansible-playbook -i inventory playbooks/netbox_setup.yml
    ansible-playbook -i inventory playbooks/netbox_vm_update.yml
