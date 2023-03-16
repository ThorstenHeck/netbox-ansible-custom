# Netbox initializer

Setup Netbox with custom Data and deploy VMs.

## execute
    export NETBOX_API_KEY=SECRET_TOKEN_CHANGE_ME
    export NETBOX_URL=http://65.21.252.14:8000

    git clone https://bitbucket.adesso-group.com/scm/aaaskub/ansible-netbox-setup.git
    cd netbox-ansible-setup
    ansible-playbook -i inventory playbooks/netbox_setup.yml
    ansible-playbook -i inventory playbooks/netbox_vm_update.yml
