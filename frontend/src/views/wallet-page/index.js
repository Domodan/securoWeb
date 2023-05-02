import React, { useEffect, useState} from 'react';

// material-ui
import { useTheme } from '@mui/material/styles';
import { Avatar, Divider, Grid, Typography } from '@mui/material';

import { gridSpacing } from '../../store/constant';

// assets
import KeyboardArrowUpOutlinedIcon from '@mui/icons-material/KeyboardArrowUpOutlined';
import KeyboardArrowDownOutlinedIcon from '@mui/icons-material/KeyboardArrowDownOutlined';

// project imports
import MainCard from '../../ui-component/cards/MainCard';
import SubCard from '../../ui-component/cards/SubCard';

// ==============================|| SAMPLE PAGE ||============================== //

const Wallet = () => {
    const theme = useTheme();
    const [balance, setBalance] = useState();
    const [transactions, setTransactions] = useState();

    const user = JSON.parse(localStorage.getItem("user"));

    useEffect(() => {
        // const token = localStorage.getItem("token");
        const url = `http://13.246.166.173/api/wallets/${user.id}`;
        // const header = new Headers({
        //     Accept: "application/json",
        //     "Content-Type": "application/json",
        //     "Authorization": `Bearer ${token}`,
        // });
        fetch(url)
        .then(response => response.json())
        .then((data) => {
            if (data?.success === "True") {
                const wallet_data = data.data
                if (wallet_data.length === 1) {
                    const wallet = wallet_data[0];
                    setBalance(wallet.available_balance);
                }
            }
        })
        .catch(error => console.error(error));
    }, [user]);
    
    useEffect(() => {
        // const token = localStorage.getItem("token");
        const url = `http://13.246.166.173/api/transactions/${user.id}`;
        // const header = new Headers({
        //     Accept: "application/json",
        //     "Content-Type": "application/json",
        //     "Authorization": `Bearer ${token}`,
        // });
        fetch(url)
        .then(response => response.json())
        .then((data) => {
            console.log("Transaction Response:", data);
            if (data?.success === "True") {
                setTransactions(data.data);
            }
        })
        .catch(error => console.error(error));
    }, []);
    
    return (
        <MainCard title="My Wallet">
            <Grid item xs={12} sx={{marginBottom: 5}}>
                <Grid container spacing={gridSpacing}>
                    <Grid item xs={12} md={6}>
                        <SubCard title="Available Balance">
                            <Grid item xs={12}>
                                <Grid container alignItems="center" justifyContent="space-between">
                                    <Grid item>
                                        <Typography variant="subtitle1" color="inherit">
                                            Balance
                                        </Typography>
                                    </Grid>
                                    <Grid item>
                                        <Grid container alignItems="center" justifyContent="space-between">
                                            <Grid item>
                                                <Typography variant="subtitle1" color="inherit">
                                                    UGX {balance}
                                                </Typography>
                                            </Grid>
                                            <Grid item>
                                                <Avatar
                                                    variant="rounded"
                                                    sx={{
                                                        width: 16,
                                                        height: 16,
                                                        borderRadius: '5px',
                                                        backgroundColor: theme.palette.success.light,
                                                        color: theme.palette.success.dark,
                                                        ml: 2
                                                    }}
                                                >
                                                    <KeyboardArrowUpOutlinedIcon fontSize="small" color="inherit" />
                                                </Avatar>
                                            </Grid>
                                        </Grid>
                                    </Grid>
                                </Grid>
                            </Grid>
                        </SubCard>
                    </Grid>
                    <Grid item xs={12} md={6}>
                        <SubCard title="Total Balance">
                            <Grid item xs={12}>
                                <Grid container alignItems="center" justifyContent="space-between">
                                    <Grid item>
                                        <Typography variant="subtitle1" color="inherit">
                                            Balance
                                        </Typography>
                                    </Grid>
                                    <Grid item>
                                        <Grid container alignItems="center" justifyContent="space-between">
                                            <Grid item>
                                                <Typography variant="subtitle1" color="inherit">
                                                    UGX {balance}
                                                </Typography>
                                            </Grid>
                                            <Grid item>
                                                <Avatar
                                                    variant="rounded"
                                                    sx={{
                                                        width: 16,
                                                        height: 16,
                                                        borderRadius: '5px',
                                                        backgroundColor: theme.palette.success.light,
                                                        color: theme.palette.success.dark,
                                                        ml: 2
                                                    }}
                                                >
                                                    <KeyboardArrowUpOutlinedIcon fontSize="small" color="inherit" />
                                                </Avatar>
                                            </Grid>
                                        </Grid>
                                    </Grid>
                                </Grid>
                            </Grid>
                        </SubCard>
                    </Grid>
                </Grid>
            </Grid>
            <Grid item xs={12}>
                <SubCard title="Transaction Summary">
                    <Grid container spacing={gridSpacing}>
                        <Grid item xs={12}>
                            {transactions && (transactions.length > 0 || Object.keys(transactions).length) ?
                            transactions.map((transaction) => {
                                <>
                                    <Grid container direction="column">
                                        <Grid item>
                                            <Grid container alignItems="center" justifyContent="space-between">
                                                <Grid item>
                                                    <Typography variant="subtitle1" color="inherit">
                                                        {transaction.transaction_date}
                                                    </Typography>
                                                </Grid>
                                                <Grid item>
                                                    <Grid container alignItems="center" justifyContent="space-between">
                                                        <Grid item>
                                                            <Typography variant="subtitle1" color="inherit">
                                                                UGX {transaction.transaction_amount}
                                                            </Typography>
                                                        </Grid>
                                                        <Grid item>
                                                            <Avatar
                                                                variant="rounded"
                                                                sx={{
                                                                    width: 16,
                                                                    height: 16,
                                                                    borderRadius: '5px',
                                                                    backgroundColor: theme.palette.success.light,
                                                                    color: theme.palette.success.dark,
                                                                    ml: 2
                                                                }}
                                                            >
                                                                <KeyboardArrowUpOutlinedIcon fontSize="small" color="inherit" />
                                                            </Avatar>
                                                        </Grid>
                                                    </Grid>
                                                </Grid>
                                            </Grid>
                                        </Grid>
                                        <Grid item>
                                            <Typography variant="subtitle2" sx={{ color: 'success.dark' }}>
                                                10% Profit
                                            </Typography>
                                        </Grid>
                                    </Grid>
                                    <Divider sx={{ my: 1.5 }} />
                                </>
                            })
                            :null}
                        </Grid>
                    </Grid>
                </SubCard>
            </Grid>
        </MainCard>
    )
};

export default Wallet;
