import { useEffect, useState } from 'react';

// material-ui
import { Grid } from '@mui/material';

// project imports
import EarningCard from './EarningCard';
import PopularCard from './PopularCard';
import TotalOrderLineChartCard from './TotalOrderLineChartCard';
import TotalIncomeDarkCard from './TotalIncomeDarkCard';
import TotalIncomeLightCard from './TotalIncomeLightCard';
import TotalGrowthBarChart from './TotalGrowthBarChart';
import { gridSpacing } from '../../../store/constant';

// ==============================|| DEFAULT DASHBOARD ||============================== //

const Dashboard = () => {
    const [isLoading, setLoading] = useState(true);
    const [balance, setBalance] = useState(500.00);
    const [expenditure, setExpenditure] = useState(961);
    const [income, setIncome] = useState(204);
    const [savings, setSavings] = useState(201);
    const user = JSON.parse(localStorage.getItem("user"));

    useEffect(() => {
        setLoading(false);
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
                    setSavings(wallet.available_balance);
                    setExpenditure(971);
                    setIncome(205);
                    localStorage.setItem("wallet_id", wallet.wallet_id);
                }
            }
        })
        .catch(error => console.error(error));
    }, [user]);

    return (
        <Grid container spacing={gridSpacing}>
            <Grid item xs={12}>
                <Grid container spacing={gridSpacing}>
                    <Grid item lg={4} md={6} sm={6} xs={12}>
                        <EarningCard isLoading={isLoading} balance={balance} />
                    </Grid>
                    <Grid item lg={4} md={6} sm={6} xs={12}>
                        <TotalOrderLineChartCard isLoading={isLoading} expenditure={expenditure} />
                    </Grid>
                    <Grid item lg={4} md={12} sm={12} xs={12}>
                        <Grid container spacing={gridSpacing}>
                            <Grid item sm={6} xs={12} md={6} lg={12}>
                                <TotalIncomeDarkCard isLoading={isLoading} income={income} />
                            </Grid>
                            <Grid item sm={6} xs={12} md={6} lg={12}>
                                <TotalIncomeLightCard isLoading={isLoading} savings={savings} />
                            </Grid>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>
            <Grid item xs={12}>
                <Grid container spacing={gridSpacing}>
                    <Grid item xs={12} md={8}>
                        <TotalGrowthBarChart isLoading={isLoading} />
                    </Grid>
                    <Grid item xs={12} md={4}>
                        <PopularCard isLoading={isLoading} />
                    </Grid>
                </Grid>
            </Grid>
        </Grid>
    );
};

export default Dashboard;
