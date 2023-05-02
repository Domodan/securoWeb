// assets
import { IconTypography, IconPalette, IconShadow, IconWindmill, IconWallet } from '@tabler/icons-react';

// constant
const icons = {
    IconTypography,
    IconPalette,
    IconShadow,
    IconWindmill,
    IconWallet
};

// ==============================|| ACCOUNT MENU ITEMS ||============================== //

const account = {
    id: 'account',
    title: 'Transactions',
    type: 'group',
    children: [
        {
            id: 'wallet',
            title: 'Wallet',
            type: 'item',
            url: '/wallet',
            icon: icons.IconWallet,
            breadcrumbs: false
        },
        {
            id: 'util-typography',
            title: 'Deposit',
            type: 'item',
            url: '/utils/util-typography',
            icon: icons.IconTypography,
            breadcrumbs: false
        },
        {
            id: 'util-color',
            title: 'Withdraw',
            type: 'item',
            url: '/utils/util-color',
            icon: icons.IconPalette,
            breadcrumbs: false
        },
        {
            id: 'util-shadow',
            title: 'Reports',
            type: 'item',
            url: '/utils/util-shadow',
            icon: icons.IconShadow,
            breadcrumbs: false
        },
        {
            id: 'icons',
            title: 'Mobile Money',
            type: 'collapse',
            icon: icons.IconWindmill,
            children: [
                {
                    id: 'tabler-icons',
                    title: 'Airtel Money',
                    type: 'item',
                    url: '/icons/tabler-icons',
                    breadcrumbs: false
                },
                {
                    id: 'material-icons',
                    title: 'MTN MoMo',
                    type: 'item',
                    url: '/icons/material-icons',
                    breadcrumbs: false
                }
            ]
        }
    ]
};

export default account;
