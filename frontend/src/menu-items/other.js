// assets
import { IconBrandChrome, IconHelp, IconWallet } from '@tabler/icons-react';

// constant
const icons = { IconBrandChrome, IconHelp, IconWallet };

// ==============================|| SAMPLE PAGE & DOCUMENTATION MENU ITEMS ||============================== //

const other = {
    id: 'sample-docs-roadmap',
    type: 'group',
    children: [
        {
            id: 'sample-page',
            title: 'Others',
            type: 'item',
            url: '/wallet',
            icon: icons.IconWallet,
            breadcrumbs: false
        },
        // {
        //     id: 'documentation',
        //     title: 'Documentation',
        //     type: 'item',
        //     url: 'https://codedthemes.gitbook.io/berry/',
        //     icon: icons.IconHelp,
        //     external: true,
        //     target: true
        // }
    ]
};

export default other;
