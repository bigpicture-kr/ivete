import {
    MOBILE_BREAK_POINT,
    XD_DESKTOP_WIDTH,
    XD_LAPTOP_WIDTH,
    XD_MOBILE_WIDTH,
    XD_TABLET_WIDTH
  } from "../constants/Variables";
  import styleStringGenerator from "../utils/styleStringGenerator";
  import { pxToRem, pxToRemMo } from "./Size";
  
  const customMediaQuery = (maxWidth: number): string =>
    `@media (max-width: ${maxWidth}px)`;
  
  const mediaQueryGenerator = (
    styles: { key: string; value: number | string }[]
  ): string => {
    return (
      `${customMediaQuery(MOBILE_BREAK_POINT)} {
        ${styleStringGenerator(styles, pxToRemMo)}
      }` +
      `${customMediaQuery(XD_MOBILE_WIDTH)} {
        ${styleStringGenerator(styles, pxToRem)}
      }`
    );
  };
  
  export const media = {
    custom: customMediaQuery,
    desktop: customMediaQuery(XD_DESKTOP_WIDTH),
    laptop: customMediaQuery(XD_LAPTOP_WIDTH),
    tablet: customMediaQuery(XD_TABLET_WIDTH),
    mobileBreak: customMediaQuery(MOBILE_BREAK_POINT),
    mobile: customMediaQuery(XD_MOBILE_WIDTH),
    mediaQueryGenerator
  };
  