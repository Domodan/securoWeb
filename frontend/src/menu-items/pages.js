// assets
// import { IconKey } from '@tabler/icons-react';

// // constant
// const icons = {
//     IconKey
// };
// assets
import { IconWallet, IconUserPlus, IconShadow, IconWindmill, IconLogin, IconLogout, IconLock, IconLockOpen } from '@tabler/icons-react';

// constant
const icons = {
    IconShadow,
    IconWindmill,
    IconLogin,
    IconLock,
    IconWallet,
    IconUserPlus
};

// ==============================|| EXTRA PAGES MENU ITEMS ||============================== //

const pages = {
    id: 'pages',
    title: 'Account',
    // caption: 'Pages Caption',
    type: 'group',
    children: [
        {
            id: 'login3',
            title: 'Login',
            type: 'item',
            url: '/pages/login/login3',
            target: true,
            icon: icons.IconLogin,
            breadcrumbs: false
        },
        {
            id: 'register3',
            title: 'Register',
            type: 'item',
            url: '/pages/register/register3',
            target: true,
            icon: icons.IconUserPlus,
            breadcrumbs: false
        },
        {
            id: 'password',
            title: 'Change Passwords',
            type: 'item',
            url: '/pages/register/register3',
            target: true,
            icon: icons.IconLock,
            breadcrumbs: false
        },
    ]
    // children: [
    //     {
    //         id: 'authentication',
    //         title: 'Authentication',
    //         type: 'collapse',
    //         icon: icons.IconKey,

    //         children: [
    //             {
    //                 id: 'login3',
    //                 title: 'Login',
    //                 type: 'item',
    //                 url: '/pages/login/login3',
    //                 target: true
    //             },
    //             {
    //                 id: 'register3',
    //                 title: 'Register',
    //                 type: 'item',
    //                 url: '/pages/register/register3',
    //                 target: true
    //             }
    //         ]
    //     },
    //     {
    //         id: 'admin',
    //         title: 'System Admin',
    //         type: 'collapse',
    //         icon: icons.IconKey,

    //         children: [
    //             {
    //                 id: 'login3',
    //                 title: 'User Accounts',
    //                 type: 'item',
    //                 url: '/pages/login/login3',
    //                 target: true
    //             },
    //             {
    //                 id: 'register3',
    //                 title: 'Transactions',
    //                 type: 'item',
    //                 url: '/pages/register/register3',
    //                 target: true
    //             },
    //             {
    //                 id: 'password',
    //                 title: 'Change Passwords',
    //                 type: 'item',
    //                 url: '/pages/register/register3',
    //                 target: true
    //             },
    //         ]
    //     }
    // ]
};

export default pages;
