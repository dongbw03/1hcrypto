declare module 'astro:content' {
	interface RenderResult {
		Content: import('astro/runtime/server/index.js').AstroComponentFactory;
		headings: import('astro').MarkdownHeading[];
		remarkPluginFrontmatter: Record<string, any>;
	}
	interface Render {
		'.md': Promise<RenderResult>;
	}

	export interface RenderedContent {
		html: string;
		metadata?: {
			imagePaths: Array<string>;
			[key: string]: unknown;
		};
	}
}

declare module 'astro:content' {
	type Flatten<T> = T extends { [K: string]: infer U } ? U : never;

	export type CollectionKey = keyof AnyEntryMap;
	export type CollectionEntry<C extends CollectionKey> = Flatten<AnyEntryMap[C]>;

	export type ContentCollectionKey = keyof ContentEntryMap;
	export type DataCollectionKey = keyof DataEntryMap;

	type AllValuesOf<T> = T extends any ? T[keyof T] : never;
	type ValidContentEntrySlug<C extends keyof ContentEntryMap> = AllValuesOf<
		ContentEntryMap[C]
	>['slug'];

	/** @deprecated Use `getEntry` instead. */
	export function getEntryBySlug<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		// Note that this has to accept a regular string too, for SSR
		entrySlug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;

	/** @deprecated Use `getEntry` instead. */
	export function getDataEntryById<C extends keyof DataEntryMap, E extends keyof DataEntryMap[C]>(
		collection: C,
		entryId: E,
	): Promise<CollectionEntry<C>>;

	export function getCollection<C extends keyof AnyEntryMap, E extends CollectionEntry<C>>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => entry is E,
	): Promise<E[]>;
	export function getCollection<C extends keyof AnyEntryMap>(
		collection: C,
		filter?: (entry: CollectionEntry<C>) => unknown,
	): Promise<CollectionEntry<C>[]>;

	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(entry: {
		collection: C;
		slug: E;
	}): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(entry: {
		collection: C;
		id: E;
	}): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof ContentEntryMap,
		E extends ValidContentEntrySlug<C> | (string & {}),
	>(
		collection: C,
		slug: E,
	): E extends ValidContentEntrySlug<C>
		? Promise<CollectionEntry<C>>
		: Promise<CollectionEntry<C> | undefined>;
	export function getEntry<
		C extends keyof DataEntryMap,
		E extends keyof DataEntryMap[C] | (string & {}),
	>(
		collection: C,
		id: E,
	): E extends keyof DataEntryMap[C]
		? Promise<DataEntryMap[C][E]>
		: Promise<CollectionEntry<C> | undefined>;

	/** Resolve an array of entry references from the same collection */
	export function getEntries<C extends keyof ContentEntryMap>(
		entries: {
			collection: C;
			slug: ValidContentEntrySlug<C>;
		}[],
	): Promise<CollectionEntry<C>[]>;
	export function getEntries<C extends keyof DataEntryMap>(
		entries: {
			collection: C;
			id: keyof DataEntryMap[C];
		}[],
	): Promise<CollectionEntry<C>[]>;

	export function render<C extends keyof AnyEntryMap>(
		entry: AnyEntryMap[C][string],
	): Promise<RenderResult>;

	export function reference<C extends keyof AnyEntryMap>(
		collection: C,
	): import('astro/zod').ZodEffects<
		import('astro/zod').ZodString,
		C extends keyof ContentEntryMap
			? {
					collection: C;
					slug: ValidContentEntrySlug<C>;
				}
			: {
					collection: C;
					id: keyof DataEntryMap[C];
				}
	>;
	// Allow generic `string` to avoid excessive type errors in the config
	// if `dev` is not running to update as you edit.
	// Invalid collection names will be caught at build time.
	export function reference<C extends string>(
		collection: C,
	): import('astro/zod').ZodEffects<import('astro/zod').ZodString, never>;

	type ReturnTypeOrOriginal<T> = T extends (...args: any[]) => infer R ? R : T;
	type InferEntrySchema<C extends keyof AnyEntryMap> = import('astro/zod').infer<
		ReturnTypeOrOriginal<Required<ContentConfig['collections'][C]>['schema']>
	>;

	type ContentEntryMap = {
		"en": {
"daily/2026-06-01-btc-eth-analysis.md": {
	id: "daily/2026-06-01-btc-eth-analysis.md";
  slug: "daily/2026-06-01-btc-eth-analysis";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/bitcoin-bulls-eye-fresh-positions-after-btc-price-drops-under-71k.md": {
	id: "news/bitcoin-bulls-eye-fresh-positions-after-btc-price-drops-under-71k.md";
  slug: "news/bitcoin-bulls-eye-fresh-positions-after-btc-price-drops-under-71k";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/bitcoin-volatility-is-down-56-but-analysts-still-expect-up-to-20-btc-price-move.md": {
	id: "news/bitcoin-volatility-is-down-56-but-analysts-still-expect-up-to-20-btc-price-move.md";
  slug: "news/bitcoin-volatility-is-down-56-but-analysts-still-expect-up-to-20-btc-price-move";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/bitmine-acquires-26497-eth-as-it-targets-a-slower-approach-to-5-of-ethereums-tot.md": {
	id: "news/bitmine-acquires-26497-eth-as-it-targets-a-slower-approach-to-5-of-ethereums-tot.md";
  slug: "news/bitmine-acquires-26497-eth-as-it-targets-a-slower-approach-to-5-of-ethereums-tot";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/cme-group-goes-live-with-247-crypto-futures-and-options-launches-bitcoin-volatil.md": {
	id: "news/cme-group-goes-live-with-247-crypto-futures-and-options-launches-bitcoin-volatil.md";
  slug: "news/cme-group-goes-live-with-247-crypto-futures-and-options-launches-bitcoin-volatil";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/coinbase-exec-sees-path-to-cryptos-dodd-frank-moment-as-clarity-act-heads-for-se.md": {
	id: "news/coinbase-exec-sees-path-to-cryptos-dodd-frank-moment-as-clarity-act-heads-for-se.md";
  slug: "news/coinbase-exec-sees-path-to-cryptos-dodd-frank-moment-as-clarity-act-heads-for-se";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/debate-on-clarity-act-continues-this-week-as-us-senate-returns.md": {
	id: "news/debate-on-clarity-act-continues-this-week-as-us-senate-returns.md";
  slug: "news/debate-on-clarity-act-continues-this-week-as-us-senate-returns";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/dogecoin-gains-paxos-support-in-push-for-broader-institutional-adoption.md": {
	id: "news/dogecoin-gains-paxos-support-in-push-for-broader-institutional-adoption.md";
  slug: "news/dogecoin-gains-paxos-support-in-push-for-broader-institutional-adoption";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/duckduckgo-launched-duck-ai-now-their-hit-product-is-no-ai.md": {
	id: "news/duckduckgo-launched-duck-ai-now-their-hit-product-is-no-ai.md";
  slug: "news/duckduckgo-launched-duck-ai-now-their-hit-product-is-no-ai";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/elon-musks-spacex-warns-175-billion-ipo-investors-of-potential-future-share-dilu.md": {
	id: "news/elon-musks-spacex-warns-175-billion-ipo-investors-of-potential-future-share-dilu.md";
  slug: "news/elon-musks-spacex-warns-175-billion-ipo-investors-of-potential-future-share-dilu";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/grayscale-sets-029-fee-for-its-hyperliquid-etf-undercutting-bitwise-and-21shares.md": {
	id: "news/grayscale-sets-029-fee-for-its-hyperliquid-etf-undercutting-bitwise-and-21shares.md";
  slug: "news/grayscale-sets-029-fee-for-its-hyperliquid-etf-undercutting-bitwise-and-21shares";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/japans-ruling-party-pushes-crypto-etfs-yen-denominated-stablecoins.md": {
	id: "news/japans-ruling-party-pushes-crypto-etfs-yen-denominated-stablecoins.md";
  slug: "news/japans-ruling-party-pushes-crypto-etfs-yen-denominated-stablecoins";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/nvidia-releases-its-best-open-ai-model-yetbut-still-lags-behind-china.md": {
	id: "news/nvidia-releases-its-best-open-ai-model-yetbut-still-lags-behind-china.md";
  slug: "news/nvidia-releases-its-best-open-ai-model-yetbut-still-lags-behind-china";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/strategy-bitcoin-sale-timing-throws-wrench-into-20-million-polymarket-pool.md": {
	id: "news/strategy-bitcoin-sale-timing-throws-wrench-into-20-million-polymarket-pool.md";
  slug: "news/strategy-bitcoin-sale-timing-throws-wrench-into-20-million-polymarket-pool";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/strategy-sold-32-bitcoin-and-thats-a-good-thing.md": {
	id: "news/strategy-sold-32-bitcoin-and-thats-a-good-thing.md";
  slug: "news/strategy-sold-32-bitcoin-and-thats-a-good-thing";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/strive-asst-eyes-42b-war-chest-to-ramp-up-bitcoin-accumulation.md": {
	id: "news/strive-asst-eyes-42b-war-chest-to-ramp-up-bitcoin-accumulation.md";
  slug: "news/strive-asst-eyes-42b-war-chest-to-ramp-up-bitcoin-accumulation";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/the-business-owners-guide-to-vertical-integration-with-bitcoin.md": {
	id: "news/the-business-owners-guide-to-vertical-integration-with-bitcoin.md";
  slug: "news/the-business-owners-guide-to-vertical-integration-with-bitcoin";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/ton-price-pumps-after-telegram-ceo-says-token-will-be-rebranded-to-gram.md": {
	id: "news/ton-price-pumps-after-telegram-ceo-says-token-will-be-rebranded-to-gram.md";
  slug: "news/ton-price-pumps-after-telegram-ceo-says-token-will-be-rebranded-to-gram";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/ton-revives-gram-token-brand-as-telegram-ceo-durov-says-network-is-returning-to-.md": {
	id: "news/ton-revives-gram-token-brand-as-telegram-ceo-durov-says-network-is-returning-to-.md";
  slug: "news/ton-revives-gram-token-brand-as-telegram-ceo-durov-says-network-is-returning-to-";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/trumps-business-partner-teases-future-meme-coin-plans-were-the-biggest-brand-on-.md": {
	id: "news/trumps-business-partner-teases-future-meme-coin-plans-were-the-biggest-brand-on-.md";
  slug: "news/trumps-business-partner-teases-future-meme-coin-plans-were-the-biggest-brand-on-";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
"news/unable-to-recover-from-roughly-50-million-hack-radiant-capital-is-winding-down.md": {
	id: "news/unable-to-recover-from-roughly-50-million-hack-radiant-capital-is-winding-down.md";
  slug: "news/unable-to-recover-from-roughly-50-million-hack-radiant-capital-is-winding-down";
  body: string;
  collection: "en";
  data: any
} & { render(): Render[".md"] };
};
"zh": {
"analysis/2026-05-30-10-30-BTC与ETH：缩量震荡下的十字路口，方向选择一触即发.md": {
	id: "analysis/2026-05-30-10-30-BTC与ETH：缩量震荡下的十字路口，方向选择一触即发.md";
  slug: "analysis/2026-05-30-10-30-btc与eth缩量震荡下的十字路口方向选择一触即发";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"analysis/2026-05-30-11-52-📉-BTC-区间震荡中的关键信号：看跌吞没与内包线突破的博弈.md": {
	id: "analysis/2026-05-30-11-52-📉-BTC-区间震荡中的关键信号：看跌吞没与内包线突破的博弈.md";
  slug: "analysis/2026-05-30-11-52--btc-区间震荡中的关键信号看跌吞没与内包线突破的博弈";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"analysis/2026-05-30-12-11-📉-震荡区间中的价格行为学博弈：BTC-ETH-关键信号与模拟盘持仓深度解析.md": {
	id: "analysis/2026-05-30-12-11-📉-震荡区间中的价格行为学博弈：BTC-ETH-关键信号与模拟盘持仓深度解析.md";
  slug: "analysis/2026-05-30-12-11--震荡区间中的价格行为学博弈btc-eth-关键信号与模拟盘持仓深度解析";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"analysis/2026-05-30-12-16-📉-区间震荡中的突破信号：Al-Brooks-价格行为学下的-BTC-ETH-交易复盘与策略.md": {
	id: "analysis/2026-05-30-12-16-📉-区间震荡中的突破信号：Al-Brooks-价格行为学下的-BTC-ETH-交易复盘与策略.md";
  slug: "analysis/2026-05-30-12-16--区间震荡中的突破信号al-brooks-价格行为学下的-btc-eth-交易复盘与策略";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"analysis/2026-05-30-13-01-【Al-Brooks价格行为学】BTC与ETH陷入区间震荡：突破信号密集涌现，多空博弈一触即发.md": {
	id: "analysis/2026-05-30-13-01-【Al-Brooks价格行为学】BTC与ETH陷入区间震荡：突破信号密集涌现，多空博弈一触即发.md";
  slug: "analysis/2026-05-30-13-01-al-brooks价格行为学btc与eth陷入区间震荡突破信号密集涌现多空博弈一触即发";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"daily/2026-06-01-btc-eth-analysis.md": {
	id: "daily/2026-06-01-btc-eth-analysis.md";
  slug: "daily/2026-06-01-btc-eth-analysis";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/2026-06-01-btc-etf-inflow.md": {
	id: "news/2026-06-01-btc-etf-inflow.md";
  slug: "news/2026-06-01-btc-etf-inflow";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/bitcoin-bulls-eye-fresh-positions-after-btc-price-drops-under-71k.md": {
	id: "news/bitcoin-bulls-eye-fresh-positions-after-btc-price-drops-under-71k.md";
  slug: "news/bitcoin-bulls-eye-fresh-positions-after-btc-price-drops-under-71k";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/bitcoin-volatility-is-down-56-but-analysts-still-expect-up-to-20-btc-price-move.md": {
	id: "news/bitcoin-volatility-is-down-56-but-analysts-still-expect-up-to-20-btc-price-move.md";
  slug: "news/bitcoin-volatility-is-down-56-but-analysts-still-expect-up-to-20-btc-price-move";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/bitmine-acquires-26497-eth-as-it-targets-a-slower-approach-to-5-of-ethereums-tot.md": {
	id: "news/bitmine-acquires-26497-eth-as-it-targets-a-slower-approach-to-5-of-ethereums-tot.md";
  slug: "news/bitmine-acquires-26497-eth-as-it-targets-a-slower-approach-to-5-of-ethereums-tot";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/cme-group-goes-live-with-247-crypto-futures-and-options-launches-bitcoin-volatil.md": {
	id: "news/cme-group-goes-live-with-247-crypto-futures-and-options-launches-bitcoin-volatil.md";
  slug: "news/cme-group-goes-live-with-247-crypto-futures-and-options-launches-bitcoin-volatil";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/coinbase-exec-sees-path-to-cryptos-dodd-frank-moment-as-clarity-act-heads-for-se.md": {
	id: "news/coinbase-exec-sees-path-to-cryptos-dodd-frank-moment-as-clarity-act-heads-for-se.md";
  slug: "news/coinbase-exec-sees-path-to-cryptos-dodd-frank-moment-as-clarity-act-heads-for-se";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/debate-on-clarity-act-continues-this-week-as-us-senate-returns.md": {
	id: "news/debate-on-clarity-act-continues-this-week-as-us-senate-returns.md";
  slug: "news/debate-on-clarity-act-continues-this-week-as-us-senate-returns";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/dogecoin-gains-paxos-support-in-push-for-broader-institutional-adoption.md": {
	id: "news/dogecoin-gains-paxos-support-in-push-for-broader-institutional-adoption.md";
  slug: "news/dogecoin-gains-paxos-support-in-push-for-broader-institutional-adoption";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/duckduckgo-launched-duck-ai-now-their-hit-product-is-no-ai.md": {
	id: "news/duckduckgo-launched-duck-ai-now-their-hit-product-is-no-ai.md";
  slug: "news/duckduckgo-launched-duck-ai-now-their-hit-product-is-no-ai";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/elon-musks-spacex-warns-175-billion-ipo-investors-of-potential-future-share-dilu.md": {
	id: "news/elon-musks-spacex-warns-175-billion-ipo-investors-of-potential-future-share-dilu.md";
  slug: "news/elon-musks-spacex-warns-175-billion-ipo-investors-of-potential-future-share-dilu";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/grayscale-sets-029-fee-for-its-hyperliquid-etf-undercutting-bitwise-and-21shares.md": {
	id: "news/grayscale-sets-029-fee-for-its-hyperliquid-etf-undercutting-bitwise-and-21shares.md";
  slug: "news/grayscale-sets-029-fee-for-its-hyperliquid-etf-undercutting-bitwise-and-21shares";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/japans-ruling-party-pushes-crypto-etfs-yen-denominated-stablecoins.md": {
	id: "news/japans-ruling-party-pushes-crypto-etfs-yen-denominated-stablecoins.md";
  slug: "news/japans-ruling-party-pushes-crypto-etfs-yen-denominated-stablecoins";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/nvidia-releases-its-best-open-ai-model-yetbut-still-lags-behind-china.md": {
	id: "news/nvidia-releases-its-best-open-ai-model-yetbut-still-lags-behind-china.md";
  slug: "news/nvidia-releases-its-best-open-ai-model-yetbut-still-lags-behind-china";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/strategy-bitcoin-sale-timing-throws-wrench-into-20-million-polymarket-pool.md": {
	id: "news/strategy-bitcoin-sale-timing-throws-wrench-into-20-million-polymarket-pool.md";
  slug: "news/strategy-bitcoin-sale-timing-throws-wrench-into-20-million-polymarket-pool";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/strategy-sold-32-bitcoin-and-thats-a-good-thing.md": {
	id: "news/strategy-sold-32-bitcoin-and-thats-a-good-thing.md";
  slug: "news/strategy-sold-32-bitcoin-and-thats-a-good-thing";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/strive-asst-eyes-42b-war-chest-to-ramp-up-bitcoin-accumulation.md": {
	id: "news/strive-asst-eyes-42b-war-chest-to-ramp-up-bitcoin-accumulation.md";
  slug: "news/strive-asst-eyes-42b-war-chest-to-ramp-up-bitcoin-accumulation";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/the-business-owners-guide-to-vertical-integration-with-bitcoin.md": {
	id: "news/the-business-owners-guide-to-vertical-integration-with-bitcoin.md";
  slug: "news/the-business-owners-guide-to-vertical-integration-with-bitcoin";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/ton-price-pumps-after-telegram-ceo-says-token-will-be-rebranded-to-gram.md": {
	id: "news/ton-price-pumps-after-telegram-ceo-says-token-will-be-rebranded-to-gram.md";
  slug: "news/ton-price-pumps-after-telegram-ceo-says-token-will-be-rebranded-to-gram";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/ton-revives-gram-token-brand-as-telegram-ceo-durov-says-network-is-returning-to-.md": {
	id: "news/ton-revives-gram-token-brand-as-telegram-ceo-durov-says-network-is-returning-to-.md";
  slug: "news/ton-revives-gram-token-brand-as-telegram-ceo-durov-says-network-is-returning-to-";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/trumps-business-partner-teases-future-meme-coin-plans-were-the-biggest-brand-on-.md": {
	id: "news/trumps-business-partner-teases-future-meme-coin-plans-were-the-biggest-brand-on-.md";
  slug: "news/trumps-business-partner-teases-future-meme-coin-plans-were-the-biggest-brand-on-";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
"news/unable-to-recover-from-roughly-50-million-hack-radiant-capital-is-winding-down.md": {
	id: "news/unable-to-recover-from-roughly-50-million-hack-radiant-capital-is-winding-down.md";
  slug: "news/unable-to-recover-from-roughly-50-million-hack-radiant-capital-is-winding-down";
  body: string;
  collection: "zh";
  data: any
} & { render(): Render[".md"] };
};

	};

	type DataEntryMap = {
		
	};

	type AnyEntryMap = ContentEntryMap & DataEntryMap;

	export type ContentConfig = never;
}
