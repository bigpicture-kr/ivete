import { pxToRem } from "../constants/Size";

const styleStringGenerator = (
  styles: { key: string; value: number | string }[],
  sizeCalculator: typeof pxToRem
): string => {
  return `${styles
    .map(
      item =>
        `${item.key}: ${
          typeof item.value === "string"
            ? item.value
            : sizeCalculator(item.value)
        }`
    )
    .join(";")}`;
};

export default styleStringGenerator;
