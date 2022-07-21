import { Link } from "react-router-dom";
import * as Styled from "./TopNav.style";

const TopNav = () => {
    return (
        <Styled.Container>
            <Link to="/">Ivete</Link>
        </Styled.Container>
    );
};

export default TopNav;
