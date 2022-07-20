// global-style.ts
import { createGlobalStyle } from "styled-components";
import { reset } from "styled-reset";
import { media } from "../constants/Media";
import { vw, vwMobile, vwTablet } from "../constants/Size";
import { ROOT_FONT_SIZE } from "../constants/Variables";

// 외부에서 import 할거니까 모듈 내보내자~!
export const GlobalStyle = createGlobalStyle`
  ${reset}

  /* 그밖에 글로벌 스타일 작성하기  */
  * {
    box-sizing: border-box;
  }

  a {
    text-decoration: none;
    cursor: pointer;
  }

  ul {
    list-style: none;
  }

  input {
    outline: none;
  }

  button {
    background-color: transparent;
    cursor: pointer;
    padding: 0;
    margin: 0; // ios default css
    border: none;
  }

  svg {
    vertical-align: top;
  }
  
  body {
    will-change: overflow-y, position;
  }

  html {
    font-size: ${vw(ROOT_FONT_SIZE)};
    will-change: font-size;
    height: 100%;
    
    ${media.laptop} {
      font-size: ${vw(ROOT_FONT_SIZE * 1.5)};
    }

    ${media.tablet} {
      font-size: ${vwTablet(ROOT_FONT_SIZE * 0.8)};
    }

    ${media.mobileBreak} {
      font-size: ${vwMobile(ROOT_FONT_SIZE * 0.5)};
    }

    ${media.mobile} {
      font-size: ${vwMobile(ROOT_FONT_SIZE)};
    }  
  }
`;
